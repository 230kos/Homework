from src.decorators import my_function


def test_my_function_ok(capsys):
    with open("mylog.txt", "r") as file:
        text = file.read()
        print(text)
        my_function(1,2)
        captured = capsys.readouterr()
        assert captured.out == "Function started\nFunction finished\nMy function ok, result 3\n\n"
