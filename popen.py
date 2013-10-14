


def popen_timeout(command, timeout=120):
    """call shell command and either return its output or kill it
    If it doesn't normally exit within timeout seconds and return None
    On using this method keep in mind that the output returned has a \n appended in the end"""
    import subprocess, signal, os, time
    from datetime import datetime
    start = datetime.now()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while process.poll() is None:
        time.sleep(0.2)
        now = datetime.now()
        if (now - start).seconds> timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return None
    return process.communicate()[0]

