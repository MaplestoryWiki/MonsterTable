# MonsterTable
The monster data of this table is crawled from [StrategyWiki](https://strategywiki.org/wiki/MapleStory). 
It provides multiple sorting and filtering on monster's level, HP, MP, PDR, MDR.


# Dependencies

To create this website:

- use [StrategyWiki crawler](https://github.com/MaplestoryWiki/StrategyWiki) to get the monster data
- The sorting and filtering features are provided by [TableFilter](http://koalyptus.github.io/TableFilter/).
- The image loading function is provided by [Lazy Load](http://appelsiini.net/projects/lazyload/).


# How to use
- run `python generate_monster_table_html.py` to create the `index.html`. It will load the monster data from the `monster.json` file.
