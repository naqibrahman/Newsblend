psql -U postgres -d newsblend -c "UPDATE newsfeed_source SET score_average=(random()*11-5)"
