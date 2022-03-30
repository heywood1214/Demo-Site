mkdir -p ~/.streamlit/

echo "\
[server]\n\
web: npm start -p $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
