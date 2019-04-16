$('.open').on('click', () => {
    var $id = $(this.event.currentTarget).attr('id');
    console.log($id);
    $('#project-'+$id).show();     
})