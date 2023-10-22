module main 
import vweb 
import db.sqlite

struct App {
			vweb.Context
	pub mut:
			db sqlite.DB
}

fn main() {
	mut app := App{
		db: sqlite.connect('blog.db')!
	}
	sql app.db {
		create table Article
	}!

	first_article := Article{
		title: 'first'
		text: 'V is great.'
		author: 'Lenon'
	}

	second_article := Article{
		title: 'Second post.'
		text: 'Hm... what should I write about?'
		author: 'Mackarty'
	}

	sql app.db {
		insert first_article into Article
		insert second_article into Article
	}!
	vweb.run(app, 8001)
}

pub fn (app &App) index() vweb.Result {
	articles := app.find_all()
	return $vweb.html()
}

['/new']
pub fn (mut app App) new() vweb.Result {
	return $vweb.html()
}