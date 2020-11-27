# coding: utf-8
import webbrowser

url_list = ['https://ar.indeed.com/Empleos-de-Sin-experiencia-en-Palermo,-Buenos-Aires','https://au.indeed.com/Part-Time-jobs-in-Melbourne-VIC','https://at.indeed.com/Reinigungskraft-Jobs-Wien','https://bh.indeed.com/Driver-jobs-in-Bahrain-International-Airport','https://emplois.be.indeed.com/Bruxelles-Emplois-Etudiant','https://www.indeed.com.br/empregos-de-SEM-Experi%C3%AAncia-em-S%C3%A3o-Paulo,-SP','https://ca.indeed.com/Full-Time-jobs-in-Calgary,-AB','https://www.indeed.cl/Empleos-de-Part-time-en-Santiago-de-Chile,-Regi%C3%B3n-Metropolitana','https://cn.indeed.com/%E5%B7%A5%E4%BD%9C-%E6%9A%91%E6%9C%9F%E5%AE%9E%E4%B9%A0%E7%94%9F-Intern-%E5%9C%B0%E7%82%B9-%E4%B8%8A%E6%B5%B7%E5%B8%82','https://co.indeed.com/Empleos-de-Trabajo-sin-experiencia-de-lunes-a-viernes-en-Bogot%C3%A1,-Cundinamarca','https://cr.indeed.com/Empleos-de-Call-center-en-Curridabat,-Provincia-de-San-Jos%C3%A9','https://cz.indeed.com/S-Ubytov%C3%A1n%C3%ADm-jobs-in-Hlavn%C3%AD-m%C4%9Bsto-Praha','https://dk.indeed.com/Deltid-jobs-in-K%C3%B8benhavn','https://ec.indeed.com/Empleos-de-Medio-tiempo-en-Quito,-Provincia-de-Pichincha','https://eg.indeed.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%B3%D8%A7%D8%A6%D9%82%D9%8A%D9%86-%D9%81%D9%8A-%D9%85%D8%AD%D8%A7%D9%81%D8%B8%D8%A9-%D8%A7%D9%84%D9%82%D8%A7%D9%87%D8%B1%D8%A9','https://www.indeed.fi/Myyj%C3%A4-jobs-in-Helsinki','https://www.indeed.fr/Paris-(75)-Emplois-Job-Etudiant','https://de.indeed.com/Minijob-Jobs-in-Berlin','https://gr.indeed.com/%CE%9F%CE%B4%CE%B7%CE%B3%CE%BF%CF%82-jobs-in-%CE%98%CE%B5%CF%83%CF%83%CE%B1%CE%BB%CE%BF%CE%BD%CE%AF%CE%BA%CE%B7','https://www.indeed.hk/English-Speaking-jobs-in-Hong-Kong-Island','https://hu.indeed.com/Alkalmi-Munka-jobs-in-Budapest','https://www.indeed.com/q-Work-From-Home-jobs.html','https://www.indeed.co.in/F-F-jobs-in-Kolkata,-West-Bengal','https://id.indeed.com/lowongan-kerja-Dibutuhkan-Segera-di-Medan','https://ie.indeed.com/Part-Time-jobs-in-County-Dublin','https://il.indeed.com/%D7%A2%D7%91%D7%95%D7%93%D7%94-%D7%9E%D7%99%D7%99%D7%93%D7%99%D7%AA-jobs-in-%D7%91%D7%90%D7%A8-%D7%A9%D7%91%D7%A2,-%D7%9E%D7%97%D7%95%D7%96-%D7%94%D7%93%D7%A8%D7%95%D7%9D','https://it.indeed.com/Roma,-Lazio-offerte-lavoro-Part-Time','https://jp.indeed.com/%E6%AD%A3%E7%A4%BE%E5%93%A1%E9%96%A2%E9%80%A3%E3%81%AE%E6%B1%82%E4%BA%BA%E5%8C%97%E6%B5%B7%E9%81%93-%E6%9C%AD%E5%B9%8C%E5%B8%82','https://kw.indeed.com/Driver-jobs-in-Kuwait-City','https://www.indeed.lu/jobs?q=Recrutement&l=Cloche+d%27Or','https://www.indeed.com.my/jobs?q=Part-time&l=Kuala+Lumpur','https://www.indeed.com.mx/Empleos-de-Medio-tiempo-en-Ciudad-de-M%C3%A9xico,-D.-F.','https://ma.indeed.com/Casablanca-emplois-Chauffeur','https://www.indeed.nl/Bijbaan-vacatures-in-Rotterdam','https://nz.indeed.com/Student-Part-Time-jobs-in-Auckland-City,-Auckland','https://ng.indeed.com/Vacancies-in-A-Hotel-jobs-in-Ikeja','https://no.indeed.com/Sommerjobb-jobs-in-Oslo','https://om.indeed.com/Al-Turki-Enterprises-jobs-in-Muscat','https://www.indeed.com.pk/Teacher-jobs-in-Lahore','https://pa.indeed.com/Empleos-de-Sin-experiencia-en-Provincia-de-Panam%C3%A1','https://www.indeed.com.pe/Empleos-de-Para-adulto-mayor-en-Miraflores,-Lima','https://www.indeed.com.ph/Poea-Job-Hiring-jobs-in-POEA','https://pl.indeed.com/Praca-Kierowca-C-E-w-Niemcy,-zagranica','https://www.indeed.pt/ofertas?q=Part+Time&l=Lisboa','https://qa.indeed.com/Driver-jobs-in-Doha-International-Airport','https://ro.indeed.com/Asistent-Medical-jobs-in-Bucure%C8%99ti','https://ru.indeed.com/%D0%A1%D1%80%D0%BE%D1%87%D0%BD%D0%BE-%D0%A2%D1%80%D0%B5%D0%B1%D1%83%D1%8E%D1%82%D1%81%D1%8F-jobs-in-%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0','https://sa.indeed.com/%D8%A7%D9%84%D9%8A%D9%88%D9%85-jobs-in-%D9%85%D9%86%D8%B7%D9%82%D8%A9-%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6','https://www.indeed.com.sg/%E6%96%B0%E5%8A%A0%E5%9D%A1-jobs','https://www.indeed.co.za/Admin-jobs-in-Cape-Town,-Western-Cape','https://kr.indeed.com/%EC%9E%85%EC%A3%BC-%EC%9A%94%EC%96%91%EB%B3%B4%ED%98%B8%EC%82%AC-%EA%B5%AC%EC%9D%B8%EC%A7%81-%EC%B7%A8%EC%97%85-%EC%84%9C%EC%9A%B8-%EC%A7%80%EC%97%AD','https://www.indeed.es/Ofertas-de-Para-extranjeros-en-Madrid-provincia','https://se.indeed.com/Sommarjobb-jobb-i-Stockholms-L%C3%A4n','https://www.indeed.ch/Offerte-Lavoro-Jobs-in-Lugano,-TI','https://tw.indeed.com/%E5%85%A8%E5%9C%8B%E5%B0%B1%E6%A5%ADe%E7%B6%B2-jobs-in-%E5%8F%B0%E6%9D%B1%E7%B8%A3-%E5%8F%B0%E6%9D%B1%E5%B8%82','https://th.indeed.com/%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9E%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%87%E0%B8%B2%E0%B8%99-%E0%B8%AB%E0%B8%A2%E0%B8%B8%E0%B8%94%E0%B9%80%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B9%8C-%E0%B8%AD%E0%B8%B2%E0%B8%97%E0%B8%B4%E0%B8%95%E0%B8%A2%E0%B9%8C%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5','https://tr.indeed.com/%C5%9Eof%C3%B6r-jobs-in-Istanbul','https://ua.indeed.com/%D0%95%D0%B6%D0%B5%D0%B4%D0%BD%D0%B5%D0%B2%D0%BD%D0%B0%D1%8F-%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D0%A5%D0%B0%D1%80%D1%8C%D0%BA%D0%BE%D0%B2','https://www.indeed.ae/Walk-Interview-jobs-in-Dubai','https://www.indeed.co.uk/Part-Time-jobs-in-London','https://uy.indeed.com/Empleos-de-Empresa-de-limpieza-en-Montevideo,-Departamento-de-Montevideo','https://ve.indeed.com/Editorial-notitarde-jobs-in-Valencia,-Carabobo','https://vn.indeed.com/Vi%E1%BB%87c-l%C3%A0m-L%C6%B0%C6%A1ng-7-Tri%E1%BB%87u-t%E1%BA%A1i-H%C3%A0-N%E1%BB%99i']

chrome_path = 'open /usr/bin/google-chrome\\ Chrome.app %s'

for url in url_list:
	webbrowser.get(chrome_path).open_new(url)