#!/bin/bash


# Creating ./results directory and corresponding subdirectories for metrics and statistical data, in case they do not exist. For example if the repository has just been downloaded and they have not been created yet.
mkdir ./results
mkdir ./results/metrics
mkdir ./results/statistical-data


# Deleting previous metrics, so that they don't interfere with the ones we want to measure with the current network status
rm ./results/metrics/ztna-metrics.txt
rm ./results/metrics/non-ztna-metrics.txt


# Execute transfers
for i in $(seq 1 50); do
  curl -s -w "@./utilities/metrics-format/ztna-metrics-format.txt" http://orion.openziti.eu:8080/version >> ./results/metrics/ztna-metrics.txt #ZTNA
  echo "Executed $i ZTNA transfers."
done

for i in $(seq 1 50); do
  curl -s -w "@./utilities/metrics-format/non-ztna-metrics-format.txt" http://orion.nonztna.openziti.eu:1027/version >> ./results/metrics/non-ztna-metrics.txt #non-ZTNA
  echo "Executed $i non-ZTNA transfers."
done


# Deleting statistical data excluded from previous metrics, so that they don't interfere with the ones we want to exclude from the measurements conducted with the current network status
rm ./results/statistical-data/ztna-statistical-data.txt
rm ./results/statistical-data/non-ztna-statistical-data.txt


# Extract statistical data from transfers' metrics
python3 ./utilities/python-utilities/statistical-data-extraction.py ./results/metrics/ztna-metrics.txt >> ./results/statistical-data/ztna-statistical-data.txt
python3 ./utilities/python-utilities/statistical-data-extraction.py ./results/metrics/non-ztna-metrics.txt >> ./results/statistical-data/non-ztna-statistical-data.txt 


# Create "columns" suitable for printing with paste command
python3 ./utilities/python-utilities/column-creation.py ./results/statistical-data/ztna-statistical-data.txt >> ztna-column.txt
python3 ./utilities/python-utilities/column-creation.py ./results/statistical-data/non-ztna-statistical-data.txt >> non-ztna-column.txt


# Adding the corresponding tag on top of each "column"
echo "   ZTNA   |" | cat - ztna-column.txt > temp && mv temp ztna-column.txt
echo " non-ZTNA |" | cat - non-ztna-column.txt > temp && mv temp non-ztna-column.txt


# Print the results comparisson using the paste command
paste -d '' ./utilities/labels/curl-variables-labels.txt ./utilities/labels/statistical-variables-labels.txt ztna-column.txt non-ztna-column.txt


# Remove "column" *.txt extension files to avoid repository polution
rm ztna-column.txt
rm non-ztna-column.txt


# Inform user about generated files he can access at a later stage
echo "\n    ZTNA      metrics     saved in ./results/metrics/ztna-metrics.txt"
echo "non-ZTNA      metrics     saved in ./results/metrics/non-ztna-metrics.txt\n"
echo "    ZTNA statistical data saved in ./results/statistical-data/ztna-statistical-data.txt"
echo "non-ZTNA statistical data saved in ./results/statistical-data/non-ztna-statistical-data.txt\n"
