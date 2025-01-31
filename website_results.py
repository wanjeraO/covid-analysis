import papermill as pm

datestamp = '20200331'

ma_runs = [
    {
        'state_code': 'MA',
        'results_label': f'{datestamp}_{int(util * 100)}_util_euclidean',
        'ed_inst_max_utilization_pct': util
    } for util in (0.2, 0.4, 0.6, 0.8)
]
other_runs = [
    {
        'state_code': code,
        'results_label': f'{datestamp}_40_util_travel_time',
        'ed_inst_max_utilization_pct': 0.4
    } for code in ('NY', 'MI')
]
runs = ma_runs

if __name__ == '__main__':
    for run in runs:
        pm.execute_notebook(
            'University-hospital bed assignment.ipynb',
            'results.ipynb',
            parameters=run
    )
