# Army_Doctrine_Network
Network analysis of Army doctrine as of June 2017

This project examines the U.S. Army's doctrinal corpus as of June 2017. The main point of this project
is to iterate through .txt versions of all the Army's doctrinal texts, pull out and store every reference in each
document to any other doctrinal publication, and then build a visualization of a multi-directional network
graph using that information. This allows us to examine both the overall distribution of certain network traits
(e.g. centrality, degree, clustering) and draw conclusions about the Army's doctrine.

Only a few of the Army's doctrinal publications are included in this repository. These are meant to serve as 
examples to allow people who access this repository to run the code without having to convert all the Army's
doctrinal pubs to .txt files themselves. However I have not included everything because many of these pubs
are only accessible with Common Access Card (CAC) access to the Army Publishing Directorate (www.apd.army.mil) and I don't intend
to be responsible for spilling those documents in an unsecured fashion all over the Internet.

The following files are included in this repository:

final code.py: This code uses regular expressions to identify all references in each Army doctrinal publication
to all other Army doctrinal publications. It then removes obselete references (of which there are many) and outputs
a number of visualizations of the remaining data. Outputs from this file include the following:
          1. references_list_current.csv - contains the final data of all current Army doctrine with current associated
            current references.
          2. plot1_degree_graph.png - overall degree distribution of the Army doctrine network
          3. plot2_indegree_graph.png - visualization of the indegree distribution of the Army doctrine network
          4. plot3_outdegree_graph.png - visualization of the outdegree distribution of the Army doctrine network
          5. plot4_final_graph.png - network graph of the Army doctrine network.

code for sustainment doctrine.py: Uses the references_list_current.csv file generated by final code.py to create 
visualizations of the Army's sustainment doctrine. Outputs from this file include:
          1. plot5_sustainment_graph.png - network graph of the Army's sustainment doctrine network
          2. plot6_leadership_degree_graph.png - visualization of the overall degree distribution of the Army sustainment
            doctrine network
          3. plot7_leadership_indegree_graph.png - visualization of the indegree distribution of the Army sustainment
            doctrine network
          4. plot8_leadership_outdegree_graph.png - visualization of the outdegree distribution of the Army sustainment
            doctrine network.

code for leadership doctrine.py - Uses the references_list_current.csv file generated by final code.py to create 
visualizations of the Army's leadership doctrine (e.g. all publications connected to 6-22 series publications). Outputs
from this file include:
          1. plot9_leadership_graph.png - network graph of the Army's leadership doctrine network
          2. plot10_leadership_degree_graph.png - visualization of the overall degree distribution of the Army leadership
            doctrine network
          3. plot11_leadership_indegree_graph.png - visualization of the indegree distribution of the Army leadership
            doctrine network
          4. plot12_leadership_outdegree_graph.png - visualization of the outdegree distribution of the Army leadership
            doctrine network.
            
pub_timeline.py: Uses the doc_with_dates.csv file to calculate how frequently the Army has published new doctrine
since 2012.

word count.py: Calculates how long it would take an average reader to read all of the Army's doctrine. Interested parties
should note that the total number of documents (331) that this code uses to make these calculations does not include a 
significant number of classified or otherwise generally unavailable publications.
            
