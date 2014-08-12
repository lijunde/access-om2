
from __future__ import print_function

from nose.plugins.attrib import attr

from model_test_setup import ModelTestSetup
import subprocess as sp
import os
import shlex

class TestBuild(ModelTestSetup):

    def __init__(self):
        super(TestBuild, self).__init__()

    def do_basic_build(self, exp):

        exp_path = os.path.join('payu-experiments/access/', exp)
        os.chdir(exp_path)
        cmd = 'payu build --laboratory {}'.format(self.lab_path)
        ret = sp.call(shlex.split(cmd))

        os.chdir(self.my_path)
        assert(ret == 0)

    def pre_build_cleanup(self, exes):

        for e in exes:
            if os.path.exists(e):
                os.remove(e)

    def post_build_checks(self, exes):

        for e in exes:
            assert(os.path.exists(e))

    @attr('fast')
    def test_ACCESS_OM_tiny(self):
        """
        Build executables for ACCESS-OM_tiny experiment.
        """

        matm_exe = os.path.join(self.bin_path, 'matm_nt62.exe')
        cice_exe = os.path.join(self.bin_path, 'cice_access-om_360x300_6p.exe')
        mom_exe = os.path.join(self.bin_path, 'fms_ACCESS-OM.x')
        exes = [matm_exe, cice_exe, mom_exe]

        self.pre_build_cleanup(exes)
        self.do_basic_build('access-om_tiny')
        self.post_build_checks(exes)

    @attr('fast')
    def test_ACCESS_CM_tiny(self):
        """
        Build executables for ACCESS-CM_tiny experiment.
        """

        cice_exe = os.path.join(self.bin_path, 'cice_access-cm_360x300_6p.exe')
        mom_exe = os.path.join(self.bin_path, 'fms_ACCESS-CM.x')
        exes = [cice_exe, mom_exe]
        
        self.pre_build_cleanup(exes)
        self.do_basic_build('access-cm_tiny')
        self.post_build_checks(exes)


    def test_ACCESS_OM(self):
        """
        Build executables for ACCESS-OM experiment.

        These are the same as ACCESS-OM_tiny
        """

        matm_exe = os.path.join(self.bin_path, 'matm_nt62.exe')
        cice_exe = os.path.join(self.bin_path, 'cice_access-om_360x300_6p.exe')
        mom_exe = os.path.join(self.bin_path, 'fms_ACCESS-OM.x')
        exes = [matm_exe, cice_exe, mom_exe]

        self.pre_build_cleanup(exes)
        self.do_basic_build('access-om')
        self.post_build_checks(exes)


    def test_ACCESS_CM(self):
        """
        Build executables for ACCESS-CM_tiny experiment.

        These are the same as ACCESS-CM_tiny
        """

        cice_exe = os.path.join(self.bin_path, 'cice_access-cm_360x300_6p.exe')
        mom_exe = os.path.join(self.bin_path, 'fms_ACCESS-CM.x')
        exes = [cice_exe, mom_exe]

        self.pre_build_cleanup(exes)
        self.do_basic_build('access-cm')
        self.post_build_checks(exes)


    @attr('slow')
    def test_ACCESS_OM_1440x1080(self):
        """
        Build executables for ACCESS-OM_1440x1080 experiment.
        """

        matm_exe = os.path.join(self.bin_path, 'matm_nt62.exe')
        cice_exe = os.path.join(self.bin_path, 'cice_access-om_1440x1080_192p.exe')
        mom_exe = os.path.join(self.bin_path, 'fms_ACCESS-OM.x')
        exes = [matm_exe, cice_exe, mom_exe]

        self.pre_build_cleanup(exes)
        self.do_basic_build('access-om_1440x1080')
        self.post_build_checks(exes)


    @attr('slow')
    def test_ACCESS_CM_1440x1080(self):
        """
        Build executables for ACCESS-CM_1440x1080 experiment.
        """

        cice_exe = os.path.join(self.bin_path, 'cice_access-cm_1440x1080_192p.exe')
        mom_exe = os.path.join(self.bin_path, 'fms_ACCESS-CM.x')
        exes = [cice_exe, mom_exe]

        self.pre_build_cleanup(exes)
        self.do_basic_build('access-cm_1440x1080')
        self.post_build_checks(exes)
