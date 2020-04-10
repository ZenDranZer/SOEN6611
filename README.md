SOEN6611 - Team E
=======================

In this project we are evaluating various open source projects in order to categarize the projects. We have used various different metrics and performed corelation analysis based on the output file generated by these metrics.
We need to perform various test suits in order to achieve full coverage of the project and then evaluate the project. To do so we have selected below mentioed metrics.
1. **Statement Coverage:** measurement procedure wherein the number of lines of code covered under certain circumstances is calculated based on the inputs from the users.
2. **Branch Coverage:** Branch coverage is a measurement to calculate the number of branches executed per user input.
3. **Mutation Score:** Mutation score is a testing practice wherein we check the accuracy or precision of the test cases.
4. **Cyclomatic Complexity:** Cyclomatic Complexity is the measure number of linearly independent paths that can be executed in a program.
5. **Knots** 
6. **Post-release Defect Density**

#### Various Projects Used:
1. **Apache Commons Collections** - [*project details*](https://commons.apache.org/proper/commons-collections/) , [*source-code*](https://github.com/apache/commons-collections) 
2. **Apache Commons Lang** - [*project details*](https://commons.apache.org/proper/commons-lang/) , [*source-code*](https://github.com/apache/commons-lang)
3. **Apache Commons Configuration** - [*project details*](https://commons.apache.org/proper/commons-configuration/) , [*source-code*](https://github.com/apache/commons-configurations)
4. **Apache Commons Math** - [*project details*](http://commons.apache.org/proper/commons-math/) , [*source-code*](https://github.com/apache/commons-math)

[*For all the version of all the projects, click here.*](https://drive.google.com/drive/folders/19Y22I9IVbl-mYOMSPOsxK-g_iJCwilIZ?usp=sharing)

#### File Structure:
.
├── Metric data collection
	├── metric1					# Metric 1 related all the output files.
	├── metric2					# Metric 2 related all the output files.
	├── metric3					# Metric 3 related all the output files.
	├── metric4					# Metric 4 related all the output files.
	├── metric5					# Metric 5 related all the output files.
	├── metric6					# Metric 6 related all the output files.
├── Metric data analysis
	├── MetricCorrelation				# Correlation metric level
		├── metric1&2_3				# Correlation between metric 1 and 2 with 3
		├── metric1&2_6				# Correlation between metric 1 and 2 with 6
		├── metric4_1&2				# Correlation between metric 1 and 2 with 4
		├── metric5_6				# Correlation between metric 5 with 6
	├── ProjectCorrelation				# Correlation project level
├── Documentation					# Documentation for the project
└── README.md


#### Requirements:

#### SciTools Understand:
1. Register and download a trial version of the SciTools Understand by [*clicking here.*](https://scitools.com/trial-download-3/) 
2. Click on the downloaded .exe file and install Understand.
3. Click on Continue evaluation.
4. Create a new project File -> New -> Project or (Alt + F + N + P)
5. Specify the project directory and click on create project.
6. To generate Knots report, Click on Metrics -> Export metrics or (Alt + M + E).
7. Select Knots checkbox -> Export 
**It will export a .csv file to the specified destination.**


#### Installation and Configuration for CLOC tool
Depending your operating system, one of these installation methods may work for you:
 1. npm install -g cloc                    # https://www.npmjs.com/package/cloc
 2. sudo apt-get install cloc              # Debian, Ubuntu
 3. sudo yum install cloc                  # Red Hat, Fedora
 4. sudo pacman -S cloc                    # Arch
 5. sudo pkg install cloc                  # FreeBSD
 6. sudo port install cloc                 # Mac OS X with MacPorts
  
For windows operating system, Download the latest cloc.exe and open command prompt and run the following command
prompt>cloc-1.84

                       cloc -- Count Lines of Code

Usage:
    cloc-1.84.exe [options] <file(s)/dir(s)/git hash(es)>
        Count physical lines of source code and comments in the given files
        (may be archives such as compressed tarballs or zip files) and/or
        recursively below the given directories or git commit hashes.
        Example:    cloc src/ include/ main.c

    cloc-1.84.exe [options] --diff <set1>  <set2>
        Compute differences of physical lines of source code and comments
        between any pairwise combination of directory names, archive
        files or git commit hashes.
        Example:    cloc --diff Python-3.5.tar.xz python-3.6/

cloc-1.84.exe --help  shows full documentation on the options.
https://github.com/AlDanial/cloc has numerous examples and more information.

#### Configuration for Mutation Testing test
The following steps provides the execution and evaluation process of mutation testing
 1. Copy the plugin into the pom file of your java project.
 2. plugin---
			<plugin> 
			<groupId> org.pitest </groupId> 
			<artifactId> pitest-maven </artifactId> 
			<version> LATEST </version> 
			<configuration> 
				<outputFormats> 
					<param> HTML </param> 
					<param> CSV </param> 
				</outputFormats> 
			</configuration> 
			</plugin>
 3. Execute mvn clean install
 4. Execute mvn org.pitest:pitest-maven:mutationCoverage -X
 5. A .csv file is create showing various mutaion score of every mutation test that has been applied to the project.
 6. Execute the ClassMutationScore.py generator to generate class wise mutation score.


#### Team members:


| Student ID  | Name | Email ID |
| ------------- | ------------- | ------------- |
| 40089272 | Hetvi Shah | hetvishah171995@gmail.com |
| 40071098  | Khyatibahen Pragajibhai Chaudhary | khyati.chaudhary1996@gmail.com |
| 40081458 | Sarvesh Hiten Vora  | vorasarvesh99@gmail.com |
| 40091187 | Satish Chanda | sathishchandas@gmail.com |
| 40080924 | Venkat Mani Deep Chandana  | venkatmanideep553@gmail.com  |
