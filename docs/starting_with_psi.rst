===============================
Tutorial: Starting with PSI Matrices
===============================

This tutorial demonstrates how to use **subsplice** to perform feature selection
and clustering of splicing events. We will start from a PSI (Percent Spliced In) file (in form of a text file or a matrix in a h5ad slot),
select variable features, and then perform clustering to find the splicing subtypes (clusters comprised of samples).

Installation
------------

We recommend creating a fresh conda environment with Python **3.11** or higher
(any version > 3.10 works):

.. code-block:: bash

   conda create -n subsplice-env python=3.11
   conda activate subsplice-env

Then install the latest version of ``subsplice`` using ``pip``:

.. code-block:: bash

   pip install subsplice


Test the Installation
---------------------

After installation, open Python and check that the package imports correctly:

.. code-block:: python

   import subsplice as ss
   print(ss.__version__)

You should see:

.. code-block::

   0.0.0

If you see this version number without errors, you are ready to continue.


Step 1: Import the package
--------------------------

First, import the package:

.. code-block:: python

   import subsplice as ss


Step 2: Load a PSI file
-----------------------

Provide the path to your PSI file and load it with
:func:`subsplice.read_psi_file`:

.. code-block:: python

   psi_file_path = '/Users/THA8TF/Desktop/Hs_RNASeq_top_alt_junctions-PSI_EventAnnotation-75p.txt'

   psi, metadata = ss.read_psi_file(psi_file_path, n_metadata_cols=11)


Step 3: Feature Selection
-------------------------

Select variable features from the PSI matrix using
:func:`subsplice.find_variable_features`:

.. code-block:: python

   variable_features, psi, metadata = ss.find_variable_features(
       psi, metadata,
       fold_threshold=0.2,
       samples_differing=4,
       corr_threshold_intercorr=0.2,
       corr_n_events=10,
       corr_threshold=0.8,
       write_files=False,
       savedir=None,
       speed='og'
   )


Step 4: Run OncoSplice
----------------------

Finally, perform clustering with :func:`subsplice.find_subtypes`:

.. code-block:: python

   final_clusters, de_results = ss.find_subtypes(
       psi=psi,
       metadata=metadata,
       variable_features=variable_features,
       pca_corr_threshold=0.4,
       npcs=30,
       rank='k30',
       force_broad='on',
       min_group_size=5,
       dPSI=0.1,
       dPSI_p_val=0.05,
       min_differential_events=100,
       top_n_differential_events=150,
       conservation='stringent',
       depletion_corr_threshold=0.4,
       speed='og',
       n_rounds=3,
       write_files=False,
       savedir=None
   )


Results
-------

After running the workflow:

- ``final_clusters`` will contain the clustering results.
- ``de_results`` will contain the differential splicing results.

You can save these outputs or visualize them as needed.
