import json

indexHtml = '''
<!DOCTYPE html>
<html>
<head>
    <title>MapleStory Monster Table</title>
</head>

<body>

<table id="monsters" width="90%%" align="center">
    <thead>
        <tr>
            <th>Name</th>
            <th>Level</th>
            <th>HP</th>
            <th>MP</th>
            <th>PDR (&#37;)</th>
            <th>MDR (&#37;)</th>
            <th>Note</th>
        </tr>
    </thead>
    <tbody>
%s
    </tbody>
</table>

<script src="tablefilter/tablefilter.js"></script>

<script data-config>
    var filtersConfig = {
        base_path: 'tablefilter/',

        paging: {
          results_per_page: ['Records: ', [10, 25, 50, 100]]
        },

        alternate_rows: true,
        rows_counter: {
            text: 'Monsters: '
        },

        col_types: [
            'string', 'number', 'number',
            'number', 'number', 'number',
            'string'
        ],

        btn_reset: true,
        auto_filter: true,
        auto_filter_delay: 1000, //milliseconds

        loader: true,
        status_bar: true,
        mark_active_columns: true,
        highlight_keywords: true,

        extensions:[{ name: 'sort' }]
    };

    var tf = new TableFilter('monsters', filtersConfig);
    tf.init();

</script>
</body>
</html>
'''


if __name__ == '__main__':
    # generate
    with open('monster.json', 'r') as fin, open('index.html','w') as fout:
        tableLines = []
        for line in fin:
            data = json.loads(line)
            tableLines.append('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(
                                data['monName'],
                                data['monLvl'],data['monHP'],
                                data['monMP'],data['monPDR'],
                                data['monMDR'],data['monEXP'],
                            ))

        fout.write(indexHtml%('\n'.join(tableLines)).encode('utf-8'))