# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RMisc3d(RPackage):
    """A collection of miscellaneous 3d plots, including isosurfaces."""

    homepage = "https://cran.r-project.org/web/packages/misc3d/index.html"
    url      = "https://cran.r-project.org/src/contrib/misc3d_0.8-4.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/misc3d"

    version('0.8-4', 'aefa27e67a243c21a1046868540343fe')
