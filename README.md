# About The Project
<img src="https://developer.spotify.com/images/guidelines/design/icon3@2x.png" alt="Spotify's logo">

As a music enthusiast, I've always been fascinated by Spotify's end-of-year Wrapped feature. To delve deeper into my music preferences, I developed a Python script that parses ```JSON``` files containing my Spotify data, which I obtained directly sourced from Spotify's records.

# Built With
The script was developed using Python with basic programming constructs such as loops, if statements and dictionary sorting. Additionally, I integrated the Tkinter module to create a user-friendly interface for selecting the ```JSON``` files.

# Getting Started
To run the application, you must first set up the project locally by following these instructions.

## Prerequisites
Check whether Python is already installed with
```
python --version
```
If Python is not installed, you can do so from the [Python website](https://www.python.org/downloads) by selecting the appropriate installer for your required environment.

To get your Spotify data, you'll need to request it through your <a href="https://www.spotify.com/account/privacy/?_ga=2.64874150.884709572.1724867443-1369734665.1707232595">Privacy Settings</a> after logging in to your account. If the link doesn't work, navigate to your Account > Security and Privacy > Privacy Settings > Download Your Data. Afterwards, you should receive an email containing your Spotify data in a ```ZIP``` file.

## Installation
After setting up Python, you can install the application to your local environment with the following instructions:
1. Clone the repo
   ```
   git clone https://github.com/Sukhman25K/Spotify-Data-Parser.git
   ```
2. Install any missing Python packages by replacing the name in the command 
   ```
   python -m pip install name
   ```


## Usage
You can go ahead and run the application when it's finished and store it in your local environment. The application can be run in different ways where the first one would be using a terminal. Navigate to the folder where the application is stored and type:
```
python Spotify-Data-Parser.py
```

Another way to run the application would be by using an IDLE such as Python's default IDLE or a code editor such as VS code. When the file explorer window shows up after running the script, navigate to where your Spotify data is held and select any files named ```StreamingHistory0.json``` or similarly numbered files, such as ```StreamingHistory1.json```, ```StreamingHistory2.json```, etc
