{
  "title": "Granular COVID-19 Data US (NYT)",
  "description": """Granular data (county level) about the spread of COVID-19
                  in the USA. Sourced from The New York Times,
                  https://github.com/nytimes/covid-19-data""",
  "licenses": [{"name": "copyright-authors"}],
  "fields": [
      {
       "name": "country",
       "description": "Geographical location - country",
       "type": "str"
       },
      {
       "name": "state",
       "description": "Geographical location - state",
       "type": "str"
       },
      {
       "name": "county",
       "description": "Geographical location - county",
       "type": "str"
       },
      {
       "name": "fips",
       "description": "Geographical location - FIPS code",
       "type": "str"
       },
      {
       "name": "date",
       "description": "Date",
       "type": "datetime"
       },
      {
       "name": "cum_cases",
       "description": """Cumulative number of reported cases at the given
                       location at the given time""",
       "type": "int"
       },
      {
       "name": "cum_deaths",
       "description": """Cumulative number of reported deaths at the given
                       location at the given time""",
       "type": "int"
       }
      ],
  "keywords": [
    "US",
    "COVID-19",
    "spread"
  ]
}