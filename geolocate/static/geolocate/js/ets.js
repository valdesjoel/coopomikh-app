$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      beforeSend: function () {
        $("#modal-ets .modal-content").html("");
        $("#modal-ets").modal("show");
      },
      success: function (data) {
        $("#modal-ets .modal-content").html(data.html_form);
      }
    });
  };


  /* Binding */

  // Create book
  $(".js-voir-ets").click(loadForm);

});
