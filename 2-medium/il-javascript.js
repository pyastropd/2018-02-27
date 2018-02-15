
$("button").click(function(e){        /// quando premo un elemento "button", esegui questa funzione
    e.preventDefault();               /// Non ricaricare la pagina

    var form=$(this).closest("form"); /// In quale form mi trovo?

    var dati_grezzi = {};             /// Oggetto vuoto per contenere i dati del form

    $.each(form.serializeArray(), function() { /// Per ogni elemento del form, associa nomi e valori.
        dati_grezzi[this.name] = +this.value;  /// Già che ci sono trasformo in float.
    });

    /// Preparo i dati a seconda che venga chiamata la simulazione o il fit
    var toserver,dati_stringa,function_to_call;

    if (form.attr("id")=="simuform"){
        dati_stringa = JSON.stringify(dati_grezzi);    /// Devo mandare al server una stringa (JSON)
        toserver = {simudata:dati_stringa};            /// Serve al server per sapere che python chiamare
        function_to_call=scatter;                      /// > in scatterplot.js

    }    else if (form.attr("id")=="fitform"){
        dati_grezzi.sim=d3.selectAll("circle").data(); /// Riprendo i dati contenuti nei pallini (bleah)
        dati_stringa = JSON.stringify(dati_grezzi);    /// Devo mandare al server una stringa (JSON)
        toserver = {fitdata:dati_stringa};             /// Serve al server per sapere che python chiamare
        function_to_call=line;                         /// > in scatterplot.js
    }

    /// Mando tutto al PHP
    $.ajax({
        type: 'GET',                      /// Che metodo uso?
        url: './roba-server.php',         /// A che file lo mando?
        data: toserver,                   /// Che cosa mando?
        dataType: 'json'                  /// Che tipo di dati?
    })
	.done( function( data ) {         /// Che cosa dico se tutto va bene?
	    console.log('OK!');           /// Guarda nella console del browser (F12)!
            function_to_call(data);       /// in scatterplot.js
	})
	.fail( function( data ) {         /// Che cosa dico se qualcosa va storto?
	    console.log('Oh, no!');       /// Guarda nella console del browser (F12)!
	});

}); /// button click
