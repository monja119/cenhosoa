var view = document.getElementById('view');
var response_title = document.getElementById('response_title');
var user_id = document.getElementById('id');
var home_view = document.getElementById('homepage');

var domain = 'http://localhost:8000/'

// if view bas is null
if(view == null){
    var url = document.getElementById('url').value;
    window.location.href = domain + "rooter/?url=" + url;
};

// setting home page view
home_view.style.height = '100vh';


// function that allows us to make query in the child tags
function goto(tabulation, template, variable, id_content){
    var xhttp = new XMLHttpRequest();
    xhttp.onprogress = function(){
    var content =  document.getElementById(id_content);
        content.innerHTML = `
            <p style="text-align:center" class="mt-5">
                <img src="/app/static/images/pigeon.gif">
            </p>
        `;
    }
    xhttp.onload = function() {
        // changing innerHTML
        var content =  document.getElementById(id_content);
        content.innerHTML = this.responseText;

        // make the url_id input in the available screen
        if(document.getElementById('url_id')){
            var url_id =  document.getElementById('url_id').value;
            window.location.href = '#' + url_id;
        };

        // some child tag somewhere
        // bar asa
        if(document.getElementById('left-bar-fin')){
            var leftBarFin =  document.getElementById('left-bar-fin');
                leftBarFin.style.height =  screen.height + 'px';
                document.onscroll = function(){
                    var window_top = window.scrollY;
                    leftBarFin.style.marginTop = - parseInt(window_top) + 'px';
                    leftBarFin.style.marginBottom =  parseInt(window_top) + 'px';
                }
        }

        // bar fampianarana
        if(document.getElementById('left-fampianarana')){
            var leftBarFin =  document.getElementById('left-fampianarana');
                leftBarFin.style.height =  screen.height + 'px';
                document.onscroll = function(){
                    var window_top = window.scrollY;
                    leftBarFin.style.marginTop = - parseInt(window_top) + 'px';
                    leftBarFin.style.marginBottom =  parseInt(window_top) + 'px';
                }
        }
    };
    xhttp.open("GET", domain + "goto/?tab="+ tabulation +"&template=" + template +"&id="+ variable, true);
    xhttp.send();

}

// a function allows us to download something
function downloader(database, id, tag_id){
    var xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        document.getElementById(tag_id).download = this.response;
    }
    xhttp.open('GET', domain + 'download/?db=' + database +'&id=' + id, true);
    xhttp.send();
}

// function to allow us to change page in the parent tag
function link(link, response_title){
    var xhttp = new XMLHttpRequest();
    xhttp.onprogress = function(){
        var content =  document.getElementById("content-sudo");
        content.innerHTML = 'Loading';
    }
    xhttp.onload = function() {
        var content =  document.getElementById("content");
        var title = document.getElementById('title');

        // changing url page
        history.pushState({}, null, domain + link);
        title.innerHTML = response_title;
        content.innerHTML = this.responseText;

        // make avaible a tag on screen view
        if(document.getElementById('url_id')){
            var id =  document.getElementById('url_id').value;
            window.location.href = '#' + id;
        };

        // some tag somewhere
        // vaovaompiangonana
        if(document.getElementById('vaovao')){
            var search_date = document.getElementById('search_date');
            goto('vaovao', null, null, 'content-context');
            search_date.onclick = function(){
                var year = document.getElementById('year').value;
                var month = document.getElementById('month').value;
                var day = document.getElementById('day').value;
                goto('vaovao', 'search_date', year + '-' + month + '-' + day, 'content-context');
                // tab, template, variable, idcontent
            }

            var select = document.getElementById('order-type');
            select.onchange = function(){
            goto('vaovao', 'order_sokajy', this.value, 'content-context')
            }
        }

        // fiangonana
        if(document.getElementById('fiangonana')){
            goto('fiangonana', 'fandaharana', null, 'content-context');
        };

        // mofonaina
        if(document.getElementById('espace-pasteur')){
            var content = document.getElementById('mofonaina');
            var popup_content = document.getElementById('popup_mofonaina');
            popup_content.hidden = true;
            popup_content.style.backgroundColor = 'black';
            popup_content.style.border = '1px solid black';
            popup_content.style.position = 'absolute';
            popup_content.style.zIndex = '1';

            document.getElementById('btn-plus').onclick = function(){
            popup_content.hidden = false;
            }

            document.getElementById('manafoana').onclick = function(){
            popup_content.hidden = true;
            }

        };


    };
    xhttp.open("GET", domain + link, true);
  xhttp.send();
}
// initiate value
link(view.value, response_title.value);

// updating data
function update(view, arg, key){
    // formatting data
    var data = [];

    if(view == 'mofonaina'){
        var title = document.getElementById('title_' + key).value;
        var content = document.getElementById('content_fanitsiana_' + key).value;
        data = key+'///'+title+'///'+content;

    }

    // sending query
    var xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        var content =  document.getElementById("content");
        content.innerHTML = this.responseText;
    }
    // http://localhost:8000/update/?view=my-view&arg=my_arg&data=my_data
    xhttp.open('GET', domain + 'update/?view=' + view +'&arg=' + arg + '&data=' + data);
    xhttp.send()
}

// removing data
function remove(database, arg, data){
    var xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        var content =  document.getElementById("content");
        content.innerHTML = this.responseText;
    }
    // http://localhost:8000/remove/?view=my-view&arg=my_arg&data=my_data
    xhttp.open('GET', domain + 'remove/?view=' + database +'&arg=' + arg + '&data=' +data);
    xhttp.send()
}


// on scrolling script (animation)
document.onscroll = function() {
            // screen
       // var screen_top_offset = window.scrollY;
       // var screen_bottom_offset = screen_top_offset + window.innerHeight;
            // tag element
       // var element_top_offset = element.offsetTop;
       // var element_bottom_offset = element_top_offset + element.offsetHeight;

       var screen_top_offset = window.scrollY;
       var screen_bottom_offset = screen_top_offset + window.innerHeight;

       // tabulation animation
       var tab = document.getElementById('tab');
       var search = document.getElementById('search');

       var tab_top_offset = tab.offsetTop;
       var tab_bottom_offset = tab_top_offset + tab.offsetHeight;


       if(screen_bottom_offset > tab_top_offset){
            tab.style.marginLeft = '0%';
            search.style.marginTop = '0%';

       } else{
            tab.style.marginLeft = '-100%';
            search.style.marginTop = '50%';
       }

}

// displayer some content
function display_content(parent_id, content_id){
    var content = document.getElementById(content_id);
    var parent = document.getElementById(parent_id);
    parent.style.height = 'auto';
    parent.style.backgroundColor = 'white';
    parent.style.color = 'black';
    content.style.visibility = 'visible';
}

// displayer of all mofonaina
function display_mofonaina(parent_id, content_id, content_loko){
    var content = document.getElementById(content_id);
    var parent = document.getElementById(parent_id);
    var loko=document.getElementById(content_loko);

    // parent
    parent.style.height = 'auto';
    content.hidden = false;
    loko.hidden = false;

    // color change
    loko.onchange = function(){
        if(loko.value == 'Mainty'){
            parent.style.backgroundColor = 'black';
            parent.style.color = 'white';
        }
        else{
            parent.style.backgroundColor = 'white';
            parent.style.color = 'black';
        }
    }
}

function display_mofonaina_fanitsiana(parent_id){
    document.getElementById(parent_id).hidden = false;
}

function manafona_mofonaina_fanitsiana(parent_id){
    document.getElementById(parent_id).hidden = true;
}

// displayer popup content
function popup(content_id){
    var content = document.getElementById(content_id);
    content.hidden = false;
    content.style.backgroundColor = ' black';
}

// hidden tag
function manafoana(famantarana){
    var content = document.getElementById(famantarana);
    content.hidden = true;
}

// make disappear pigeon if screen is loaded
window.onload = function (){
    document.getElementById('loading-div').hidden = true;
}
