"""
Builds the version of Bootstrap that's in vendor/bootstrap and packages
it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_BOOTSTRAP_VERSION = "v2.1.0"


def cp(src, dest):
    # print "Copying: %s -> %s" % (src, dest)
    cmd = [
        "cp vendor/bootstrap/%s bootstrap/static/bootstrap/%s" % (src, dest),
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_BOOTSTRAP_VERSION if len(sys.argv) is 1
                else sys.argv[1],
    }
    # print "building Bootstrap %(version)s" % args
    subprocess.call(
            ["cd vendor/bootstrap && git checkout %(version)s && make" % args],
            shell=True)
    cp("docs/assets/js/bootstrap.min.js", "js/")
    cp("js/*.js", "js/")
    cp("img/*.*", "img/")
    cp("docs/assets/css/bootstrap*.css", "css/")
    cp("less/*.*", "less/")
    cp("LICENSE", "")


if __name__ == "__main__":
    main()
