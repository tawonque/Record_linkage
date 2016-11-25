# Record_linkage
Record linkage exercise with data from the Natural History Museum.

This is a project in its very early stages, so the initial script shows only a 'dummy' file with some columns of different types.

The problem to solve: there are data repositories at the Natural History Museum with duplicated records. These duplications also occur between the different repositories available to the scientific community: 

-Paleobiology database: paleobiodb.org/navigator/
-NHM data portal: data.nhm.ac.uk
-Global biodiversity information facility: gbif.org
-Taxamatach : ncbi.nlm.nih.gov/pubmed/25247892
-World registry of marine species: marinespecies.org

How to know if the records are realy duplicated? Is it worth looking for a smaple in som other institutions only to realise that it is non-existant and that it was just matter of a few typos?

The solution is simple in its concept, but requires a good deal of data formating, the comparison of strings, geographic locations, quantities in rather complex, non standard ways.

This is just the beginning, let's see how far we get...
