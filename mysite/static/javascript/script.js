var isClickable = true;

function check(event) {

    //Verifie si le nombre de click est atteint
    checkClickNumber();
    
    if (isClickable) 
        checkClick();

}

function checkClick() {
    var painting = document.getElementsByClassName('painting')[0];

    var x = event.clientX; // x de la souris
    var y = event.clientY; // y de la souris

    var height =  painting.offsetHeight; //hauteur du tableau
    var width =  painting.offsetWidth; //largeur du tableau

    var viewportOffset = painting.getBoundingClientRect();
    var top = viewportOffset.top; // y du point haut-gauche du cadre
    var left = viewportOffset.left; // x du point haut-gauche du cadre

    var nb_detail = 5;

    scaleX = width / 100;
    scaleY = height / 100;

    // controle si le clic correspond à un détail
    var num = -1;
    for (var i = 0; i < nb_detail; i++) {
        if ((x >= left + (tab[i].x * scaleX)) &&
            (x <= left + (tab[i].x * scaleX) + (tab[i].width * scaleX)) &&
            (y >= top + (tab[i].y * scaleY)) &&
            (y <= top + (tab[i].y * scaleY) + (tab[i].height * scaleY))) {
            num = i;
            break;
        }
    }


    // check le détail correct
    if (num > -1 && num < nb_detail) {
        //AJAX pas fonctionnel
        /*$.ajax({
            type : "POST",
            url : "/check_detail",
            dataType: 'json',
            data : { 'num' : num + 1}
        })*/


        tab[num].checked = true;
        var position = num + 1;
        console.log('true ' + position);
        console.log($('.footer detail-image:nth-child(' + position + ')'));
        $('.footer .detail-image:nth-child('+ position +')').addClass('check');
    }

    // check si le niveau est fini
    var end = true;
    for (var i = 0; i < nb_detail; i++) {
        if (tab[i].checked == false) {
            end = false;
            break;
        }
    }

    if (end) {
        $('.next-level').addClass("show");
    }
}

function checkClickNumber() {
    //Verifie si le nombre de click est atteint
    click--;
    if (click < 0) {
        isClickable = false;
        setTimeout(() => { isClickable = true; click = 15 ; }, 10000);
    }
}

function popUp(obj){
  if($(obj).hasClass('show')){
    $(obj).removeClass('show');
    $(obj).addClass('hide');
  } else {
    $('.popup').removeClass('show');
    $(obj).addClass('show');
  }

}

////////    TODO : une seule fonction popup    //////////
function openPopUpClue() {
    document.getElementById('popup').style.display = 'block';
}

function closePopUpClue() {
    document.getElementById('popup').style.display = 'none';
}

function OpenClueText() {
    document.getElementById('clueText').style.display = 'block';
}

function CloseClueText() {
    document.getElementById('clueText').style.display = 'none';
}

function OpenNoCluePopUp() {
    document.getElementById('noClueAvalaible').style.display = 'block';
}

function CloseNoCluePopUp() {
    document.getElementById('noClueAvalaible').style.display = 'none';
}
