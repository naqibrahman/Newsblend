rem sudo -u postgres -H -- psql -d newsblend -c "UPDATE newsfeed_source SET score_average=(random()*11-5)"

psql -U postgres -d newsblend -c "UPDATE newsfeed_source SET score_average=(random()*11-5)"
