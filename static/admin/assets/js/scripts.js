/* alertas crud antigo */
// function hideFlash() {
// 	setTimeout(() => {
// 		const obj = document.querySelector('#modalMessage')
// 		obj.className += ' hide'
// 	} , 3000)
// }
// hideFlash()

/* AJUSTA ACTIVE DO MENU */
var url_atual = window.location.href;
var menu_id = url_atual.split("/")[3];
if (menu_id == '') menu_id = 'dashboard';
$('#'+menu_id).addClass('active');

/* MASCARA PARA OS FORMS */
$(document).ready(function(){
	$('.mask_cep').mask('00000-000');
	$('.mask_tel').mask('(00) 0000-0000');
	$('.mask_cel').mask('(00) 00000-0000');
	$('.mask_cpf').mask('000.000.000-00', {reverse: true});
	$('.mask_cnpj').mask('00.000.000/0000-00', {reverse: true});
	$('.mask_moeda').mask('000.000.000.000.000,00', {reverse: true});
	$('.mask_moeda2').mask("#.##0,00", {reverse: true});

	/* Para telefone e celular */
	var SPMaskBehavior = function (val) {
		return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
	},
	spOptions = {
		onKeyPress: function(val, e, field, options) {
			field.mask(SPMaskBehavior.apply({}, arguments), options);
		}
	};
	$('.mask_tel_cel').mask(SPMaskBehavior, spOptions);

});

/* Novos alertas */
function notificacao(from, align, tipo, mensagem) {
	$.notify({
		icon: "notification_important",
		message: mensagem,
	}, {
		type: tipo,
		delay: 300,
		timer: 1500,
		placement: {
			from: from,
			align: align
		}
	});
}

/* Excluindo itens */
function excluir_item(nome_recurso, id_item) {
	swal({
		title: 'Excluir',
		text: 'Tem certeza que deseja excluir este item?',
		type: 'warning',
		showCancelButton: true,
		confirmButtonText: 'Sim, excluir!',
		cancelButtonText: 'Não',
		confirmButtonClass: "btn btn-primary",
		cancelButtonClass: "btn btn-danger",
		buttonsStyling: false
	}).then((result) => {
		if (result.value) {
			xhr = new XMLHttpRequest();
			xhr.open('DELETE', '/' + nome_recurso + '/' + id_item + '/');
			xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			xhr.onload = function() {
				if (xhr.readyState !== 4) return;
				if (xhr.status === 200) {
					window.location.reload();
				} else {
					alert('Erro ' + xhr.status);
				}
			};
			xhr.send();
		}
	});
}