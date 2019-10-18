from subprocess import Popen, PIPE


def test_invoke_list():
    """ test run: inv -l"""
    args = ['invoke', '-l']
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    assert not stderr
    lines = [l.strip() for l in stdout.decode().split('\n') if l.strip()]
    assert lines
    for line in lines:
        assert line
