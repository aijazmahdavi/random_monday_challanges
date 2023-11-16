import random
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

# Global Variables
this_month = timezone.now().month
this_day = timezone.now().day


# List of Challenges

list_of_challenges = [
    "Learn and practice a new foreign word or phrase every day",
    "Write a short 100-word story daily",
    "Organize and clean up your email inbox",
    "Start running 20 minutes daily except Sundays",
    "Create a budget for the month",
    "Learn to cook a new recipe",
    "Research and follow a TED talk on a random topic daily except Sundays",
    "Do a quick mindfulness exercise for 10 minutes daily",
    "Set up a plant in home or office",
    "Read a chapter from a non-fiction book 20 pages per day except Sundays",
    "Learn a new coding concept daily",
    "Practice a new SEO strategy for your website/SocialMedia",
    "Take an online course on a topic you're interested in",
    "Try a 20-minute drawing challenge daily except Sunday",
    "Write down three business ideas daily except Sunday",
    "Listen to a podcast on entrepreneurship except Sunday",
    "Set specific goals for the month",
    "Review your website's analytics daily except Sunday",
    "Reach out to a potential client or partner",
    "Research a new technology trend daily except Sunday",
    "Write a blog post or article daily except Sunday",
    "Update your LinkedIn profile daily except Sunday",
    "Experiment with a new WordPress plugin and master it",
    "Learn a new keyboard shortcut daily except Sunday",
    "Watch a documentary on a technological innovation daily except Sunday",
    "Plan your social media content for the month",
    "Learn a new HTML or CSS trick daily except Sunday",
    "Explore a new app or software tool daily except Sunday",
    "Try a new SEO keyword research tool daily except Sunday",
    "Create a 20-minute presentation on a tech topic daily except Sunday",
    "Take a short online quiz to test your IT knowledge daily except Sunday",
    "Explore a new coding framework for the Month",
    "Write down your business values and mission",
    "Follow a tutorial on YouTube related to your interests",
    "Network with someone in your industry",
    "Review your website's user experience daily except Sunday",
    "Try a speed-reading exercise with a tech-related book daily except Sunday",
    "Brainstorm marketing ideas for your business for 20 minutes daily except Sunday",
    "Optimize your website's loading speed for 20 minutes daily except Sunday",
    "Learn a new technology-related acronym daily except Sunday",
    "Create a 20-minute marketing plan daily except Sunday",
    "Try a 20-minute brainstorming session on random topic daily except Sunday",
    "Practice speed typing for coding for 20 minutes daily except Sunday",
    "Learn a new concept in digital marketing daily except Sunday",
    "Follow a tutorial on JavaScript",
    "Experiment with a new WordPress theme and master it",
    "Test a new SEO strategy on a blog post",
    "Don't play mobile games for a month",
    "Don't play PC games for a month",
    "Don't take tea for a month",
    "Don't use Facebook for a month"
]

list_of_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

list_of_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# random challenge picker
pick_random_challenge = random.choice(list_of_challenges)
concatenation_random_challenge = f"<h1>{pick_random_challenge}</(h1>"

# A random Challenge
def random_challenge(request):
    return HttpResponse(concatenation_random_challenge)

# this day
def random_challenge_current_day(request):
      return HttpResponse(concatenation_random_challenge)

# this Month
def random_challange_current_month(request):
      return HttpResponse(concatenation_random_challenge)
# Random Daily Challenge
def random_daily_challenge(request):
        concatenation_random_daily_challenge = f"<h1>{pick_random_challenge}</h1>"
        return HttpResponse(concatenation_random_daily_challenge)


# Random Challenge for Month
def random_monthly_challenge(request, month):
    for month in list_of_months:
        concatenation_random_monthly_challenge = f"<h1>{pick_random_challenge}</(h1>"
        return HttpResponse(concatenation_random_monthly_challenge)

