var view = document.getElementById('view_sudo').value;
var id = document.getElementById('id_sudo').value;

if(view == null){
    var url = document.getElementById('url').value;
    window.location.href = "http://localhost:8000/rooter/?url=" + url;
};

function sudo(sudo, link, id){
    var xhttp = new XMLHttpRequest();
    xhttp.onprogress = function(){
    var content =  document.getElementById("content-sudo");

        content.innerHTML = `
            <p style="text-align:center" class="mt-5">
                <img src="/app/static/images/pigeon.gif">
            </p>
        `;
    }
    xhttp.onload = function() {
        var content =  document.getElementById("content-sudo");
        content.innerHTML = this.responseText;

        // if url by id
        if(document.getElementById('url_id')){
            var url_id =  document.getElementById('url_id').value;
            window.location.href = '#' + url_id;
        };

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
    xhttp.open("GET", "http://localhost:8000/sudoQuery/?sudo="+ sudo +"&q=" + link +"&id="+ id, true);
  xhttp.send();
}

function popup(content_id){
    var content = document.getElementById(content_id);
    var body = document.body;
    var cancel = document.getElementById('cancel_popup');

    content.style.visibility = 'visible';
    content.style.backgroundColor = ' black';

    // cancel popup
    cancel.onclick = function(){
        content.style.visibility = 'hidden';
    }



}

function manafoana(famantarana){
    var content = document.getElementById(famantarana);
    content.style.visibility = 'hidden';
}

function display_content(parent_id, content_id){
    var content = document.getElementById(content_id);
    var parent = document.getElementById(parent_id);
    parent.style.height = 'auto';
    parent.style.backgroundColor = 'white';
    parent.style.color = 'black';
    content.style.visibility = 'visible';
}


// vaovaompiangonana
if(document.getElementById('vaovao')){
    var sudo_id = document.getElementById('id_sudo').value;
    var search_date = document.getElementById('search_date');
    sudo('vaovao', null,sudo_id);
    search_date.onclick = function(){
        var year = document.getElementById('year').value;
        var month = document.getElementById('month').value;
        var day = document.getElementById('day').value;

        sudo('vaovao', year + '-' + month + '-' + day, sudo_id);
    }
}

