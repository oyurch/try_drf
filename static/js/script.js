const search = instantsearch({
  appId: 'TRU9XRWXYK',
  apiKey: '0de3977573029c30dbec37e426c852fd',
  indexName: 'blog_index',
  routing: true
});


  // initialize SearchBox
  search.addWidget(
    instantsearch.widgets.searchBox({
      container: '#search-box',
      placeholder: 'Search for products'
    })
  );

  search.addWidget(
    instantsearch.widgets.hits({
      container: '#hits',
      templates: {
        empty: 'No results',
        item: '<em>Hit {{objectID}}</em>: {{{_highlightResult.name.value}}}'
      }
    })
  )

search.start();
