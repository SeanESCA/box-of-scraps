# everyone-active

This project aims to collate data from the
[booking site for Everyone Active](https://book.everyoneactive.com/Connect/memberHomePage.aspx).
The program is entirely contained in `main.py`, and so can be executed by
running the script. Currently, it saves the ID number and name of every
centre, as well as whether they accept bookings for badminton, on the website
in `EveryoneActive.csv`.

## Results

This section details results of prodding the booking site that are not
noted in the code.

- If a login attempt fails, the username field is not cleared when the page
  reloads; only the password field is cleared.
- The timeout period is very short, estimated to be 5 minutes
  or less.
- The site consistently takes longer to respond to changing the search date
  than changing the centre.

## Discussion

The booking site does not have the address of each centre. There is a list on
[their main website](https://www.everyoneactive.com/centre/); however,
the number of centres on both sites is different, and different names
are occasionally used for the same centre.

## Contributing

My original motivation for this project was to create a tool like
[Sportscanner](https://www.sportscanner.co.uk/), but for searching for whole
badminton courts instead of places in a badminton session.
A badminton centre in London usually uses only one of several booking sites,
like:
[Lambeth Active](https://lambethcouncil.bookings.flow.onl/),
[Better](https://www.better.org.uk/), and
[SchoolHire](https://schoolhire.co.uk/). The data from these sites
can be used to make it more convenient to check the availability of badminton
courts nearby.
This project provides a good start towards that goal, but will probably not be
continued because I personally no longer need it.
Still, if you want to help expand this project, let's get in touch!
