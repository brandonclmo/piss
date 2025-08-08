--- STEAMODDED HEADER
--- MOD_NAME: New jokers
--- MOD_ID: REALPEAK
--- MOD_AUTHOR: [natehiggers]
--- MOD_DESCRIPTION: Absolute cinema 
--- PREFIX: realpeak
--- 
--- 

SMODS.Atlas{
      key = 'JOKERS', 
     path = 'gay.png', 
     px = 69, 
     py = 69, 
    

}

SMODS.Joker{
    key = 'gay', --joker key
    loc_txt = { -- local text
        name = 'Gay',
        text = {
          'If played hand contains no straight,',
          'Gives x0.1 mult'
        }
    },
    atlas = 'JOKERS', -- match the key above exactly
    rarity = 3, --rarity: 1 = Common, 2 = Uncommon, 3 = Rare, 4 = Legendary
    cost = 10, --cost
    unlocked = true, --where it is unlocked or not: if true, 
    discovered = true, --whether or not it starts discovered
    blueprint_compat = true, --can it be blueprinted/brainstormed/other
    eternal_compat = false, --can it be eternal
    perishable_compat = false, --can it be perishable
    pos = {x = 0, y = 0}, --position in atlas, starts at 0, scales by the atlas' card size (px and py): {x = 1, y = 0} would mean the sprite is 71 pixels to the right
    config = {
    extra = {
        Xmult = 1.0 
    }
    },
    loc_vars = function(self, info_queue, center)
        return {vars = {string.format("%.1f", center.ability.extra.Xmult)}}
    end,
    calculate = function(self, card, context)
        if context.before then
            card.ability.extra.Xmult = 1.0
        end
        if context.joker_main then
            return {
                card = card,
                Xmult_mod = card.ability.extra.Xmult,
                message = 'X' .. string.format("%.1f", card.ability.extra.Xmult),
                colour = G.C.MULT
            }
        end
        if context.after then
            if context.hand_type ~= 'Straight' then
                card.ability.extra.Xmult = card.ability.extra.Xmult + 0.1
                G.E_MANAGER:add_event(Event({
                    func = function()
                    -- create_floating_text('Gay Mult +0.1x', card, nil, G.C.MULT, true) -- ahhh it doesnt work fuck you game 
                        return true
                    end
                }))
            end
        end
    end
}