


function create_component() {
	mkdir -p $1/templates/$1 2>/dev/null
	touch $1/__init__.py 2>/dev/null
	touch $1/$1.py 2>/dev/null
	[[ ! -z "$2" ]] && touch $1/templates/$1/$2
}

create_component dergi
create_component dergi view.html
