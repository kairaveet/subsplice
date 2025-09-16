import subsplice as ss

# Set path to the file which contains the PSI matrix (splicing events by samples matrix)
psi_file_path = '/Users/THA8TF/Desktop/Hs_RNASeq_top_alt_junctions-PSI_EventAnnotation-75p.txt'

# Check the PSI matrix for any splicing event metadata.
# In my example, I have 11 metadata columns so I separate them from PSI values when reading in the file
psi, metadata = ss.read_psi_file(psi_file_path, n_metadata_cols=11)

# find the highly variable features which will determine the splicing subtypes
var_feats, psi, metadata = ss.find_variable_features(psi, metadata,
                                                     fold_threshold=0.2, samples_differing=4,
                                                     corr_threshold_intercorr=0.2, corr_n_events=10,
                                                     corr_threshold=0.8, write_files=False, savedir=None, speed='og')

# finally, find the patient/sample subtypes based on PSI values
final_clusters, de_results = ss.find_subtypes(psi=psi, metadata=metadata, variable_features=var_feats,
                                              pca_corr_threshold=0.4, npcs=30, rank='k30',
                                              force_broad='on', min_group_size=5, dPSI=0.1, dPSI_p_val=0.05,
                                              min_differential_events=100, top_n_differential_events=150,
                                              conservation='stringent', depletion_corr_threshold=0.4,
                                              speed='og', n_rounds=3, write_files=False, savedir=None)

