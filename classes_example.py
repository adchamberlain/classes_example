# Simple example of using classes in Python to group together methods and initial values, rather than using dictionaries and lists.
# This allows all values and functions to be hidden from API users if needed. 
#
# Andrew Chamberlain, Ph.D.
# achamberlain.com
#
# September 2019

# Define the class "employer".
class Employer(object):    

    # Initialize parameters for the employer object. 
    def __init__(self, name, city, numEmps, industry, ratings=None):
        self.name = name
        self.city = city
        self.numEmps = numEmps
        self.industry = industry
        self.ratings = ratings or {}

    # Add a method to add new ratings to an employer.
    def setRating(self, job, rating):
        self.ratings[job] = rating

    # Add a method to get the rating back for a specific job.
    def getRating(self, job):
        return self.ratings[job]

    # Add a method to calcuate the mean employer rating.  
    def getMeanRating(self):
        return sum(self.ratings.values())/len(self.ratings)

# Define two sample employers with 2 sample ratings.
SAP = Employer("SAP", "Seattle", 5000, "Software", {"accountant":3, "software engineer":5})
Google = Employer("Google", "Mountain View", 10000, "Internet", {"accountant":2,"software engineer":4})

# Print mean employer rating.
print(SAP.getMeanRating())
print(Google.getMeanRating())

# Add a new employer rating for SAP.
SAP.setRating("zoo keeper", 5)

# Show new mean employer rating.
print(SAP.getMeanRating())

# Show all employer ratings for SAP.
print(SAP.ratings)

# Show rating for one job function.
SAP.getRating("accountant")