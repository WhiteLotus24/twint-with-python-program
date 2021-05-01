
# importing the twint module.
import twint

# starting the script.
print("Initiating the script White Lotus.\t ")

search = input("what are you looking for?: ")   # YOU CAN USE THIS LINE BY UNHASHING IT.....
city = input("what is the name of place?: ")   # YOU CAN USE THIS LINE BY UNHASHING IT....
# full body
c = twint.Config()
c.Username = input("Enter a username.: ") # YOU CAN USE THIS BY UNHASHING....
c.Output = input("name of the output file.... ")
c.Limit = str(input("Set the number of tweets.: "))
c.Store_json = True
c.Near = city
c.Since = input("enter the date for the particular tweet in format [y-m-d]: ")
c.Geo = input("enter the geographical coordinate...: ")
c.Count = True
c.Retweets = True
c.Hide_output = True
c.Popular_tweets = True
c.Members_list = [""]

 # Run command
twint.run.Search(c)

