<script>
	import { Router, Route, Link } from "svelte-routing";
	import Home from './pages/Home.svelte';
	import About from './pages/About.svelte';
	import Contact from './pages/Contact.svelte';
  </script>
  
  <style>
	/* Пример простых стилей для навигации */
	nav {
	  display: flex;
	  gap: 20px;
	  margin-bottom: 20px;
	}
  </style>
  
  <header>
	<h1>Привет, мир!</h1>
	<nav>
	  <Link to="/">Главная</Link>
	  <Link to="/about">О нас</Link>
	  <Link to="/contact">Контакты</Link>
	</nav>
  </header>
  
  <main>
	<Router>
	  <Route path="/" component={Home} />
	  <Route path="/about" component={About} />
	  <Route path="/contact" component={Contact} />
	</Router>
  </main>
  