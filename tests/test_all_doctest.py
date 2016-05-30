# -*- coding: utf-8 -*-

import doctest
import logging
import os
import sys
import unittest

from configreset import logger

logger.setLevel(logging.DEBUG)


def doctest_start(package, project_dir):
    sys.path.append(project_dir)
    doctest_package(package, project_dir)


def doctest_package(package, project_dir):
    package = os.path.join(project_dir, package)
    files = os.listdir(package)
    for f in files:
        fp = os.path.join(package, f)
        sp = fp.replace(project_dir, '')[1:]

        if os.path.isfile(fp) and f.endswith('.py'):
            cls = sp[:-3].replace('/', '.')
            if cls.endswith('__init__'):
                cls = cls[:-9]
            m = __import__(cls, globals(), locals(), '*')
            logger.debug('===================>>test:%s' % cls)
            h = doctest.testmod(m=m, verbose=True)

            assert h.failed == 0, 'failed:%s' % h.failed

        elif os.path.isdir(fp):
            doctest_package(sp, project_dir)


class DocTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_httpproxy(self):
        project_dir = os.path.dirname(os.path.dirname(__file__))
        doctest_start('httpproxy', project_dir)


if __name__ == '__main__':
    unittest.main()
