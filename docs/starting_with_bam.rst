==============================
Starting with BAM Files
==============================

This section is under active development.

This tutorial will cover using SPECTRA when starting from **BAM files** to generate PSI matrices for downstream clustering.

Example (to be updated):

.. code-block:: bash

    spectra-cli --bam_folder /path/to/bams/ --gtf path/to/annotation.gtf --output results/

or in Python:

.. code-block:: python

    from spectra import bam_processing

    bam_dir = "/path/to/bams/"
    bam_processing.generate_psi(bam_dir, annotation_gtf="path/to/annotation.gtf")

Step-by-step examples and best practices will be provided here.
