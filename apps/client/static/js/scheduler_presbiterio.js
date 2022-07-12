
Vue.component('scheduler')

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#scheduler',
    data: {
        days_week: [],
        hours_week: [],
        description: '',
        edit: false,
        active: true,
        selected_day: '',
        selected_hour: '',
        primeiro_nome: '',
        ultimo_nome: '',
        email: '',
        telefone: '',
        areas: '',
    },
    mounted() {
        axios.get('scheduler_api/days_weeks_presbytery/').then(response => {
            this.days_week = response.data
        })

    },
    methods: {
        changeWeek: function () {
            this.hours_week = []
            this.selected_hour = ''
            axios.get('scheduler_api/hours_day_presbytery/' + this.selected_day).then(response => {
                this.hours_week = response.data
            }).catch(
                function (error) {
                    console.log(error)
                }
            )
        },

        saveScheduler: function () {
            if (!this.primeiro_nome || this.primeiro_nome === '') {
                Swal.fire({
                    title: 'Ops!',
                    text: "Primeiro nome é obrigatório",
                    icon: 'error',
                    confirmButtonText: 'fechar'
                })
                return

            }
            if (!this.ultimo_nome || this.ultimo_nome === '') {
                Swal.fire({
                    title: 'Ops!',
                    text: "Último nome é obrigatório",
                    icon: 'error',
                    confirmButtonText: 'fechar'
                })
                return

            }


            if (!this.areas || this.areas === '') {
                Swal.fire({
                    title: 'Ops!',
                    text: "Selecione e área que você lidera",
                    icon: 'error',
                    confirmButtonText: 'fechar'
                })
                return

            }

            let data = {
                "name": this.primeiro_nome + ' ' + this.ultimo_nome,
                "email": this.email,
                "cellphone": this.telefone.replace(/[^0-9]/g, ''),
                "days_week": this.selected_day,
                "hours_days": this.selected_hour,
                'areas': this.areas
            };

            axios.post('scheduler_api/scheduler_presbytery/', data).then(
                response => {
                    Swal.fire({
                        title: 'Deu tudo certo com sua escolha',
                        text: `A Sua escolha foi,  ${response.data.nome_day} às ${response.data.nome_hora}`,
                        icon: 'success',
                        confirmButtonText: 'Cool'
                    }).then((result) => {
                        window.location.reload();
                    })

                }

            ).catch(
                function (error) {
                    let errorText = ''
                    try {

                        for (var prop in error.response.data) {

                            for (let index = 0; error.response.data[prop].length > index; index++) {
                                errorText += `${error.response.data[prop][index]}  <br>`
                                console.log(errorText)
                            }
                            console.log('error')

                        }
                    } catch (error) {
                        errorText = error
                    }
                    Swal.fire({
                        title: 'Ops!',
                        html: errorText,
                        icon: 'error',
                        confirmButtonText: 'fechar'
                    }).then((result) => {
                        window.location.reload();
                    })
                }
            )
        }
    }
})