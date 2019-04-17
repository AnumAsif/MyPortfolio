window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("pb-navbar").style.top = "0";
  } else {
    document.getElementById("pb-navbar").style.top = "-50px";
  }
}

$('.open').on('click', () => {
    var $id = $(this.event.currentTarget).attr('id');
    console.log($id);
    $('#project-'+$id).show();     
})

$('.nav-item').on('click', ()=>{
  $('#myNavbar').hide();
})
$('#toggle-btn').on('click', ()=>{
  $('#myNavbar').toggle();
})