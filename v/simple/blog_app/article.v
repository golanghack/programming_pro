module main 
import vweb

struct Article {
	id int [primary; sql: serial]
	title string 
	text string
	author string
}

pub fn (app &App) find_all() []Article {
	return sql app.db {
		select from Article
	} or { panic(err) }
}

[post]
pub fn (mut app App) new_article(title string, text string, author string) vweb.Result {
	if title == '' || text == '' || author == '' {
		return app.text('No articles yet')
	}
	article := Article{
		title: title
		text: text 
		author: author
	}
	println(article)
	sql app.db {
		insert article into Article
	} or { panic(err) }
	return app.redirect('/')
}

['/articles'; get]
pub fn (mut app App) articles() vweb.Result {
	articles := app.find_all()
	return app.json(articles)
}