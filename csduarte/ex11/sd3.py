import os

def prompt_enter():
    raw_input("Press Enter to Continue")

print "Welcome to Super Form 4000"
prompt_enter()
print "With just 3 questions we can predict the year of your death"
prompt_enter()

print "What year were you born?",
birth_year = raw_input()

print "What is your favorite movie?",
favorite_movie = raw_input()

print "What year do you think you'll die?",
estimated_year = raw_input()

print "Thank you for your answers."
print "Calculating..."
prompt_enter()

print "Just Kidding. We can't calculate that with just 3 questions. We need 4, duh."
