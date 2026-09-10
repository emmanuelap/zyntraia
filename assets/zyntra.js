/* ============================================================================
   Zyntra - comportamiento del sitio.

   Vanilla, sin dependencias, con defer. Todo lo que anima respeta
   prefers-reduced-motion: es regla del sistema, no un extra.
   ========================================================================== */
(function () {
    'use strict';

    var quieto = window.matchMedia('(prefers-reduced-motion: reduce)');

    /* ---------------------------------------------------------- 1. header */

    var header = document.querySelector('.site-header');
    var progreso = document.getElementById('scroll-progress');

    function alScrollear() {
        var y = window.pageYOffset || document.documentElement.scrollTop;
        if (header) header.classList.toggle('is-scrolled', y > 8);
        if (progreso) {
            var alto = document.documentElement.scrollHeight - window.innerHeight;
            progreso.style.width = (alto > 0 ? (y / alto) * 100 : 0) + '%';
        }
    }

    if (header || progreso) {
        alScrollear();
        window.addEventListener('scroll', alScrollear, { passive: true });
        window.addEventListener('resize', alScrollear, { passive: true });
    }

    /* ----------------------------------------------------- 2. menu mobile */

    var toggle = document.getElementById('menu-toggle');
    var menu = document.getElementById('mobile-menu');

    if (toggle && menu) {
        var cerrar = function () {
            menu.hidden = true;
            toggle.setAttribute('aria-expanded', 'false');
            toggle.setAttribute('aria-label', 'Abrir menú');
        };
        toggle.addEventListener('click', function () {
            var abierto = menu.hidden;
            menu.hidden = !abierto;
            toggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
            toggle.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
        });
        Array.prototype.forEach.call(menu.querySelectorAll('a'), function (a) {
            a.addEventListener('click', cerrar);
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && !menu.hidden) { cerrar(); toggle.focus(); }
        });
        window.addEventListener('resize', function () {
            if (window.innerWidth >= 900 && !menu.hidden) cerrar();
        }, { passive: true });
    }

    /* --------------------------------------------------------- 3. reveal */

    var revelables = document.querySelectorAll('.reveal');
    if (revelables.length) {
        if (quieto.matches || !('IntersectionObserver' in window)) {
            Array.prototype.forEach.call(revelables, function (el) { el.classList.add('visible'); });
        } else {
            var obs = new IntersectionObserver(function (entradas) {
                entradas.forEach(function (e) {
                    if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
                });
            }, { rootMargin: '0px 0px -60px 0px', threshold: 0.05 });
            Array.prototype.forEach.call(revelables, function (el) { obs.observe(el); });
        }
    }

    /* ---------------------------------------------------- 4. calculadora */

    /* La cuenta es la misma de siempre y se mantiene a proposito:
       caidas por semana x ticket x 52. No es una promesa de resultado. */
    (function () {
        var volumen = document.getElementById('calc-volumen');
        var perdidos = document.getElementById('calc-perdidos');
        var ticket = document.getElementById('calc-ticket');
        var anual = document.getElementById('calc-anual');
        var detalle = document.getElementById('calc-detalle');
        if (!volumen || !perdidos || !ticket || !anual) return;

        var pesos = new Intl.NumberFormat('es-AR', {
            style: 'currency', currency: 'ARS', maximumFractionDigits: 0
        });

        function num(el) {
            var v = parseFloat(el.value);
            return isFinite(v) && v > 0 ? v : 0;
        }

        function calcular() {
            var v = num(volumen), p = num(perdidos), t = num(ticket);
            if (p > v) { p = v; }                    // no se pueden perder mas de las que hay
            anual.textContent = pesos.format(p * t * 52);
            if (detalle) {
                detalle.innerHTML = p
                    ? 'Son <strong>' + p + (p === 1 ? ' oportunidad' : ' oportunidades') +
                      ' por semana</strong> que se pierden. Un sistema de recordatorios y ' +
                      'seguimiento automático recupera buena parte de eso.'
                    : 'Si de verdad no se te cae ninguna, no necesitás contratarnos. ' +
                      'Probá con tus números reales.';
            }
        }

        [volumen, perdidos, ticket].forEach(function (el) {
            el.addEventListener('input', calcular);
        });
        calcular();
    }());

    /* ------------------------------------------------------ 5. carruseles */

    Array.prototype.forEach.call(document.querySelectorAll('[data-carousel]'), function (caja) {
        var slides = caja.querySelectorAll('.carousel-slide');
        var puntos = caja.querySelectorAll('.carousel-dot');
        if (slides.length < 2) return;
        var actual = 0;

        function ir(i) {
            actual = (i + slides.length) % slides.length;
            Array.prototype.forEach.call(slides, function (s, n) {
                s.classList.toggle('active', n === actual);
            });
            Array.prototype.forEach.call(puntos, function (p, n) {
                p.classList.toggle('active', n === actual);
                p.setAttribute('aria-current', n === actual ? 'true' : 'false');
            });
        }

        Array.prototype.forEach.call(puntos, function (p, n) {
            p.addEventListener('click', function () { ir(n); });
        });

        // deslizar con el dedo
        var x0 = null;
        caja.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
        caja.addEventListener('touchend', function (e) {
            if (x0 === null) return;
            var d = e.changedTouches[0].clientX - x0;
            if (Math.abs(d) > 45) ir(actual + (d < 0 ? 1 : -1));
            x0 = null;
        }, { passive: true });
    });

    /* ---------------------------------------------------------- 6. Ojito */

    /* Dos comportamientos y nada mas: parpadea cada 4-7 segundos y el iris
       sigue al cursor dentro de un radio de 0.12 del diametro. El parpado es
       la unica expresion que tiene: no le agregues nada. */
    var ojitos = document.querySelectorAll('[data-ojito]');

    if (ojitos.length && !quieto.matches) {

        Array.prototype.forEach.call(ojitos, function (ojo) {
            function parpadear() {
                ojo.classList.add('parpadea');
                setTimeout(function () { ojo.classList.remove('parpadea'); }, 150);
                setTimeout(parpadear, 4000 + Math.random() * 3000);
            }
            setTimeout(parpadear, 1500 + Math.random() * 3000);
        });

        var pendiente = false;
        window.addEventListener('pointermove', function (e) {
            if (pendiente) return;
            pendiente = true;
            requestAnimationFrame(function () {
                pendiente = false;
                Array.prototype.forEach.call(ojitos, function (ojo) {
                    var cuerpo = ojo.querySelector('.ojito-cuerpo');
                    var iris = ojo.querySelector('.ojito-iris');
                    if (!cuerpo || !iris) return;
                    var r = cuerpo.getBoundingClientRect();
                    if (r.width === 0) return;
                    var dx = e.clientX - (r.left + r.width / 2);
                    var dy = e.clientY - (r.top + r.height / 2);
                    var dist = Math.sqrt(dx * dx + dy * dy) || 1;
                    var max = r.width * 0.12;
                    var k = Math.min(1, dist / (r.width * 1.6));
                    ojo.style.setProperty('--iris-x', (dx / dist) * max * k + 'px');
                    ojo.style.setProperty('--iris-y', (dy / dist) * max * k + 'px');
                });
            });
        }, { passive: true });
    }

    /* ------------------------------------------------- 7. año del footer */

    Array.prototype.forEach.call(document.querySelectorAll('[data-anio]'), function (el) {
        el.textContent = new Date().getFullYear();
    });

}());
