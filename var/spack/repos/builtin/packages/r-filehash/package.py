# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFilehash(RPackage):
    """Implements a simple key-value style database where character string keys
    are associated with data values that are stored on the disk. A simple
    interface is provided for inserting, retrieving, and deleting data from the
    database. Utilities are provided that allow 'filehash' databases to be
    treated much like environments and lists are already used in R. These
    utilities are provided to encourage interactive and exploratory analysis on
    large datasets. Three different file formats for representing the database
    are currently available and new formats can easily be incorporated by third
    parties for use in the 'filehash' framework."""

    homepage = 'https://cran.r-project.org/'
    url      = "https://cran.r-project.org/src/contrib/filehash_2.3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/filehash"

    version('2.3', '01fffafe09b148ccadc9814c103bdc2f')
