from madlib_cli import __version__
from madlib_cli.madlib_cli import  read_template, parse, merge


def test_version():
    assert __version__ == '0.1.0'

def test_read():
    expected =['aziz','ahmad','ali']
    actual = read_template("assets/madlip_cli_test_case.txt")
    assert actual == expected

def test_parse():
    expected = 'Me and {} and {} and {} we were in the market'
    actual = parse("assets/madlip_cli_test_case.txt")
    assert expected == actual

def test_merge():
    file_path = "assets/madlip_cli_test_case.txt"
    words = read_template(file_path)
    expected = 'Me and aziz and ahmad and ali we were in the market'
    actual = merge(words,file_path)
    assert expected == actual