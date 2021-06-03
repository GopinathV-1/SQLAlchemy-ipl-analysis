from total_run import session, func, json, create_table_from_csv


def create_json(Deliveries):
    ''' creating json file from the data
        in the table'''

    # Query to pick top ten run scored RCB batsmans
    top_rcb_batsman = (session.query(
                        Deliveries.batsman,
                        func.sum(Deliveries.total_runs)).filter(
                        Deliveries.batting_team == 'RCB').group_by(
                        Deliveries.batsman).order_by(
                        func.sum(
                            Deliveries.total_runs).desc()).limit(10).all())

    top_rcb_batsman = [list(row) for row in top_rcb_batsman]
    data = {'rcb_batsman_runs': []}
    data['rcb_batsman_runs'] = top_rcb_batsman

    with open('rcb_batsman_runs.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    Deliveries = create_table_from_csv()
    create_json(Deliveries)
