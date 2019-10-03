package com.sb.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class helloworldController {

    @GetMapping("/hello")
    public String getHelloMessage(){
        return "hello melbourne";
    }
}
