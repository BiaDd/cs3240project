"""
/*

*  REFERENCES
*  Title: <HOW TO CREATE A CALENDAR USING DJANGO>
*  Author: <Hui Wen>
*  Date: <11/17/2021>
*  Code version: <N/A>
*  URL: <https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html>
*  Software License: <N/A>
*

*/

"""


from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Assignment

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter assignments by day
	def formatday(self, day, assign):
		assignments_per_day = assign.filter(due_date__day=day)
		d = ''
		for a in assignments_per_day:
			d += f'<a href="#" title="{a.description}"> {a.title} </a>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, assign):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, assign)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter assignments by year and month
	def formatmonth(self, assign, withyear=True): # takes in assignments
		assignment = assign.filter(due_date__year=self.year, due_date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, assignment)}\n'
		return cal