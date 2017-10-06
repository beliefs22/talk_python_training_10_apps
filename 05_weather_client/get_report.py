import csv
import datetime
from collections import namedtuple


def print_report(weather_json):
    """
    Prints the report information from the given json object
    :param weather_json: json objects created from json.loads
    :return: No Return
    """
    Report = namedtuple('Report', 'location temp condition')

    location = weather_json['current_observation']['display_location']['full']
    temperature = weather_json['current_observation']['temperature_string']
    condition = weather_json['current_observation']['weather']

    weather_tup = Report(location=location, temp=temperature, condition=condition)
    report_str = "The weather for {0.location} is the following:\nTemp: {0.temp}\nCondition: {0.condition}"
    print(report_str.format(weather_tup))


def check_api_use_rate():
    """
    Checks to make sure you haven't used the API more than 9 times in 8 minutes. The max you are
    allowed to use it is 10 times in 10 minutes
    :return: True if safe to use API. False if not safe to use API
    """
    with open('api_use.csv', 'r') as api_use_file:
        csv_reader = csv.reader(api_use_file)
        last_date_used_unparsed, times_used_since_last_reset_unparsed = next(csv_reader)

        month, day, year, hour, minute = [int(item)
                                          for item in last_date_used_unparsed.split("/")
                                          ]

        last_time_used = datetime.datetime(year, month, day, hour, minute)
        times_used_since_last_reset = int(times_used_since_last_reset_unparsed)

        current_time = datetime.datetime.now()

        time_since_last_use = current_time - last_time_used
        seconds_since_last_use = time_since_last_use.seconds

        # if it hasn't been ten minutes since the last time you used it
        if seconds_since_last_use < 460:
            # if it hasn't been used more than 8 times
            if times_used_since_last_reset < 9:
                # update last time use and times used
                times_used_since_last_reset += 1
                last_time_used = current_time
                print("You can use the api")
                print("You have {} uses remaining and {} minutes before the reset".format(
                    10 - times_used_since_last_reset, (460 - seconds_since_last_use) / 60.0
                ))
                update_tracker(last_time_used, times_used_since_last_reset)
                return True
            # if it has been used 8 times in the last ten minutes
            elif times_used_since_last_reset >= 9:
                print("Warning you have used the api {} times in 10 minutes.".format(
                    times_used_since_last_reset))
                return False
        # if it has been more than 9 minutes you are good to go
        elif seconds_since_last_use >= 460:
            # okay to use. reset current time and times used
            times_used_since_last_reset = 1
            last_time_used = current_time
            print("It's been more than 9 minutes since last use. You are good to go")
            update_tracker(last_time_used, times_used_since_last_reset)
            return True


def update_tracker(last_time_used: datetime, times_used_since_last_reset: int):
    """
    Updates api_use.csv file with most recent information
    :param last_time_used: Last time the API was successfully used
    :param times_used_since_last_reset: number of time you have used it in the last 8 minutes
    :return:
    """
    with open('api_use.csv', 'w') as fout:
        last_time_used_tup = last_time_used.timetuple()

        last_time_used_str = '{0.tm_mon}/{0.tm_mday}/{0.tm_year}/{0.tm_hour}/{0.tm_min}'.format(
            last_time_used_tup
        )
        csv_writer = csv.writer(fout)
        csv_writer.writerow([last_time_used_str, str(times_used_since_last_reset)])


def print_the_header():
    """
    Prints Header for Application
    :return: No Return
    """
    print('-------------------')
    print('     Weather APP')
    print('-------------------')
    print()
