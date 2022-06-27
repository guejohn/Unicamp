#!/usr/bin/env python

import argparse
import re
import sys
from os.path import isfile, join
from subprocess import PIPE, TimeoutExpired, run


class BaseTask:
    TIME_LIMIT_SECONDS = 1
    SPACES_RE = re.compile(r"\s+", re.M)

    def __init__(self, continue_on_error=True, only_matching=None):
        self.continue_on_error = continue_on_error
        self.only_matching = only_matching
        self.tested_cases = set()
        self.passed_cases = set()
        self.tested_units = set()
        self.passed_units = set()
        self.show_all_errors = False

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

    def test_one_case(self, script, in_filename_name):
        out_filename_name = in_filename_name.replace(".in", ".out")
        res_file_name = in_filename_name.replace(".in", ".res")
        self.exists(script)
        with open(in_filename_name) as i, open(out_filename_name, "w") as o:
            self.run_binary(
                ["python3", script],
                i,
                o,
                in_filename=in_filename_name,
                out_filename=out_filename_name,
            )
        assert self.compare_files(
            out_filename_name, res_file_name
        ), f'execute: diff "{out_filename_name}" "{res_file_name}"'

    def test_cases(self, script, in_filename_names, folder="testes"):
        assert type(in_filename_names) != str, "erro no caso de teste, deveria ser lista de strings"
        errors = []
        for in_filename_name in in_filename_names:
            in_filename_name = join(folder, in_filename_name)
            try:
                self.tested_cases.add(in_filename_name)
                self.test_one_case(script, in_filename_name)
                self.passed_cases.add(in_filename_name)
                print(f"  -> {in_filename_name} passou")
            except AssertionError as e:
                print(f"  -> {in_filename_name} falhou")
                errors.append(f"{e}")
                if not self.continue_on_error:
                    break
        if errors:
            assert False, "\n  -> ".join(errors)

    def input_output(self, script, input_content, expected_output):
        self.exists(script)
        p = self.run_binary(["python3", script], None, PIPE, input=input_content)
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


class Task(BaseTask):
    def teste_1_somar_datas(self):
        arquivo = "somar_datas.md"
        n_words = 60

        self.exists(arquivo)
        self.has_n_words(arquivo, n_words)

    def teste_2_lavar_maos(self):
        arquivo = "lavar_maos.md"
        n_words = 60

        self.exists(arquivo)
        self.has_n_words(arquivo, n_words)

    def teste_3_baldes(self):
        arquivo = "baldes.md"
        n_words = 60

        self.exists(arquivo)
        self.has_n_words(arquivo, n_words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Testa tarefa.")
    parser.add_argument("only", nargs="*", help="apenas unidades contendo essa string")
    parser.add_argument("-c", action="store_true", help="continua mesmo que anteriores falhem")
    args = parser.parse_args()
    Task(args.c, args.only).test_units()
