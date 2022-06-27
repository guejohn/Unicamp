#!/usr/bin/env python

import _thread
import argparse
import os
import re
import sys
import threading
from contextlib import contextmanager
from os.path import isfile, join
from subprocess import PIPE, TimeoutExpired, run


class TimeOutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeOutException(f"Tempo de {seconds}s excedido")
    finally:
        timer.cancel()


class BaseTask:
    TIME_LIMIT_SECONDS = 5
    SPACES_RE = re.compile(r"[:\s]+", re.M)

    def __init__(self, continue_on_error=True, only_matching=None):
        self.continue_on_error = continue_on_error
        self.only_matching = only_matching
        self.tested_cases = set()
        self.passed_cases = set()
        self.tested_units = set()
        self.passed_units = set()
        self.show_all_errors = False
        self.python3 = self.find_python3()
        if self.python3 is None:
            print("O Python não está no path! Verifique sua instalação")
            sys.exit(1)

    def find_python3(self):
        suffix = ".exe" if os.name == "nt" else ""
        for py in ["python3", "python", "py"]:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, py + suffix)
                if isfile(exe_file):
                    return py
        return None

    def strip_spaces(self, text):
        return self.SPACES_RE.sub(" ", text.strip())

    def read_file_utf8(self, file_name):
        assert isfile(file_name), f"Não existe o arquivo {file_name}"
        try:
            with open(file_name, encoding="utf-8", errors="strict") as f:
                return f.read()
        except ValueError:
            assert False, f"Enconding inválido em {file_name}. Por favor, use UTF-8."
        except Exception as e:  # noqa
            assert False, f"Falha ao ler arquivo {file_name}: {e}"

    def compare_stripped(self, left, right):
        return self.strip_spaces(left) == self.strip_spaces(right)

    def compare_files(self, out, res):
        left = self.read_file_utf8(out)
        right = self.read_file_utf8(res)
        return self.compare_stripped(left, right)

    def exists(self, file_name):
        assert isfile(file_name), f"você deve criar um arquivo {file_name}"

    def run_binary_inner(self, cmd, stdin, stdout, input):
        if input is None:
            p = run(
                cmd,
                stdin=stdin,
                stdout=stdout,
                encoding="utf8",
                errors="ignore",
                timeout=self.TIME_LIMIT_SECONDS,
            )
        else:
            p = run(
                cmd,
                input=input,
                stdout=stdout,
                encoding="utf8",
                errors="ignore",
                timeout=self.TIME_LIMIT_SECONDS,
            )
        assert p.returncode == 0, f"código de saída é {p.returncode}"
        return p

    def run_binary(
        self,
        cmd,
        stdin,
        stdout,
        input=None,
        in_filename=None,
        out_filename=None,
    ):
        cmd_str = " ".join([c if " " not in c and c != "" else f'"{c}"' for c in cmd])
        if in_filename:
            cmd_str += f" < {in_filename}"
        if out_filename:
            cmd_str += f" > {out_filename}"
        if input:
            cmd_str += f' com entrada "{input}"'
        try:
            return self.run_binary_inner(cmd, stdin, stdout, input)
        except AssertionError as e:
            assert False, f"falha ao executar {cmd_str} : {e}"
        except TimeoutExpired:
            assert (
                False
            ), f"falha ao executar {cmd_str} : tempo limite de {self.TIME_LIMIT_SECONDS}s excedido"

    def test_one_case(self, cmd, in_filename_name):
        out_filename_name = in_filename_name.replace(".in", ".out")
        res_file_name = in_filename_name.replace(".in", ".res")
        with open(in_filename_name) as i, open(out_filename_name, "w") as o:
            self.run_binary(
                cmd,
                i,
                o,
                in_filename=in_filename_name,
                out_filename=out_filename_name,
            )
        assert self.compare_files(
            out_filename_name, res_file_name
        ), f'execute: diff "{out_filename_name}" "{res_file_name}"'

    def test_cases(self, script, in_filename_names, args=[], folder="testes"):
        assert type(in_filename_names) != str, "erro no caso de teste, deveria ser lista de strings"
        self.exists(script)
        cmd = [self.python3, script] + args
        errors = []
        for in_filename_name in in_filename_names:
            in_filename_name = join(folder, in_filename_name)
            try:
                self.tested_cases.add(in_filename_name)
                self.test_one_case(cmd, in_filename_name)
                self.passed_cases.add(in_filename_name)
                print(f"  -> {in_filename_name} passou")
            except AssertionError as e:
                print(f"  -> {in_filename_name} falhou")
                errors.append(f"{e}")
                if not self.continue_on_error:
                    break
        if errors:
            assert False, "\n  -> ".join(errors)

    def input_output(self, script, input_content, expected_output, args=[]):
        self.exists(script)
        cmd = [self.python3, script] + args
        p = self.run_binary(cmd, None, PIPE, None, input=input_content)
        assert self.compare_stripped(
            p.stdout, expected_output
        ), f'para entrada "{input_content}", a saída é "{p.stdout.strip()}", mas era esperado "{expected_output}"'

    def should_test(self, name):
        if not name.startswith("teste_"):
            return False
        if not self.only_matching:
            return True
        for pattern in self.only_matching:
            if pattern in name:
                return True
        return False

    def test_units(self):
        for name in sorted(dir(self)):
            if not self.should_test(name):
                continue
            print()
            print(f"Executando {name}...")
            sys.stderr.flush()
            sys.stdout.flush()
            try:
                test = getattr(self, name)
                self.tested_units.add(name)
                test()
                self.passed_units.add(name)
                print(f"{name}: OK")
            except AssertionError as e:
                print(f"{name}: FALHOU")
                if "privado" not in name or self.show_all_errors:
                    print(f"  -> {e}\n")
                if not self.continue_on_error:
                    break

    def case_range(self, input_template, start, end):
        input_files = []
        for i in range(start, end + 1):
            input_files.append(input_template.format(i))
        return input_files

    def count_words(self, text):
        words = text.split()
        number_of_words = len(words)
        return number_of_words

    def has_n_words(self, file_name, n_words):
        text = self.read_file_utf8(file_name)
        assert (
            self.count_words(text) >= n_words
        ), f"{file_name} deve ter pelos menos {n_words} palavras"

    def test_clousure(self, clousure):
        import traceback

        with time_limit(self.TIME_LIMIT_SECONDS):
            try:
                clousure()
            except TimeOutException:
                assert False, f"comando excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
            except Exception:
                tb = traceback.format_exc()
                assert False, f"algum erro ocorreu durante a execução:\n{tb}"


class Task(BaseTask):
    def teste_00_testes_modulo(self):
        self.external_tested_units = set()
        self.external_passed_units = set()

        # se teste não falhar, pode carregar módulo com segurança
        def carrega_modulo():
            import teste_modulo_analise  # noqa

        self.test_clousure(carrega_modulo)
        import teste_modulo_analise

        # testa unidades externas
        for name in dir(teste_modulo_analise):
            if not self.should_test(name):
                continue
            print()
            print(f"Executando teste do módulo {name}...")
            sys.stderr.flush()
            sys.stdout.flush()
            try:
                test = getattr(teste_modulo_analise, name)

                def external_clousure():
                    test()

                self.external_tested_units.add(name)
                self.test_clousure(external_clousure)
                self.external_passed_units.add(name)
                print(f"{name}: OK")
            except AssertionError as e:
                print(f"{name}: FALHOU {e}")
                if not self.continue_on_error:
                    break

        assert (
            self.external_tested_units == self.external_passed_units
        ), "testes de unidade do módulo falharam"

    def teste_12_produtividade(self):
        script = "explorando-filmes.py"
        acao = "produtividade"
        self.exists(script)
        self.test_cases(script, self.case_range("produtividade{}.in", 1, 8), args=[acao])

    def teste_13_anos_presentes(self):
        script = "explorando-filmes.py"
        acao = "anos_presentes"
        self.exists(script)
        self.test_cases(script, self.case_range("anos_presentes{}.in", 1, 8), args=[acao])

    def teste_14_filmes_por_classificacao(self):
        script = "explorando-filmes.py"
        acao = "filmes_por_classificacao"
        self.exists(script)
        self.test_cases(script, self.case_range("filmes_por_classificacao{}.in", 1, 8), args=[acao])

    def teste_15_histograma_dos_anos(self):
        script = "explorando-filmes.py"
        acao = "histograma_dos_anos"
        self.exists(script)
        self.test_cases(script, self.case_range("histograma_dos_anos{}.in", 1, 8), args=[acao])

    def teste_16_filmes_por_pais_e_classificacao(self):
        script = "explorando-filmes.py"
        acao = "filmes_por_pais_e_classificacao"
        self.exists(script)
        self.test_cases(
            script, self.case_range("filmes_por_pais_e_classificacao{}.in", 1, 8), args=[acao]
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Testa tarefa.")
    parser.add_argument("only", nargs="*", help="apenas unidades contendo essa string")
    parser.add_argument("-c", action="store_true", help="continua mesmo que anteriores falhem")
    args = parser.parse_args()
    Task(args.c, args.only).test_units()
