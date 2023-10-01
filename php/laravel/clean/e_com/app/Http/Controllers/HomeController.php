<?php

namespace App\Http\Controllers;
use illuminate\Http\Request;

class HomeController extends Controller 
{
    public function index()
    {
        $viewData = [];
        $viewData['title'] = 'Главная - онлайн магазин Зои';
        return view('home.index')->with('viewData', $viewData);
    }

    public function about()
    {
        $data_one = 'Немного о магазине';
        $data_second = 'Немного о нас';
        $description = 'Эта страница пока в разработке...';
        $author = 'Разработка -> GolangHack';
        return view('home.about')->with('title', $data_one)
                                 ->with('subtitle', $data_second)
                                 ->with('description', $description)
                                 ->with('author', $author);
    }
}