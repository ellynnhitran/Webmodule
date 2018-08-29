import pyexcel

news = [
    {
        "link": "http://google.com",
        "title": "Google"
    },
    {
        "link": "http://facebook.com",
        "title": "Facebook"
    },
    {
        "link": "http://linkedin.com",
        "title": "LinkedIn"
    },
]

pyexcel.save_as(records=news, dest_file_name="sample.xlsx")